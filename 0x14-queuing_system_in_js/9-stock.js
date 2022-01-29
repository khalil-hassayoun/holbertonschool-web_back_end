import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const app = express();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);
const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 0 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 15 }
]
const getItemById = (id) => {
  for (const list of listProducts) {
    if (list.Id === id) return list;
  }
}
const reserveStockById = async (itemId, stock) => {
  await clientSet(itemId, stock);
}
const getCurrentReservedStockById = async (itemId) => {
  const currentReservedStock = await clientGet(itemId);
  return currentReservedStock;
}
app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)));
app.get('/list_products/:itemId', async (req, res) => {
  const id = Number(req.params.itemId);
  const item = getItemById(id);
  const currentReservedStock = await getCurrentReservedStockById(id);
  if (item) {
    item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
    res.json(item);
    return;
  }
  res.status(404).json({"status":"Product not found"});
});
app.get('/reserve_product/:itemId', async (req, res) => {
  const id = Number(req.params.itemId);
  const item = getItemById(id);
  if (!item) {
      res.status(403).json({"status":"Product not found"});
  }
  const currentReservedStock = await getCurrentReservedStockById(id);
  item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
  if ((item.stock - item.reservedStock) < 1) {
    res.status(403).json({ status: 'Not enough stock available', id });
    return;
  }
  reserveStockById(id, Number(currentReservedStock) + 1);
  res.json({ status: 'Reservation confirmed', id });
});
app.listen(1245);
