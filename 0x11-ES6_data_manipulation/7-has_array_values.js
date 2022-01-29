export default function hasValuesFromArray(set, array) {
  return array.every((num) => set.has(num));
}
