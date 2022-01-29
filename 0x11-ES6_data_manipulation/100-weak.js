export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const currCount = weakMap.get(endpoint) || 0;
  if (currCount !== undefined) weakMap.set(endpoint, currCount + 1);
  if (weakMap.get(endpoint) >= 5) throw Error('Endpoint load is high');
}
