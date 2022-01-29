export default function cleanSet(set, startString) {
  if (typeof set !== 'object') return '';
  if (typeof startString !== 'string') return '';
  if (startString.length === 0) return '';

  const tmp = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      tmp.push(element.replace(startString, ''));
    }
  });
  return tmp.join('-');
}
