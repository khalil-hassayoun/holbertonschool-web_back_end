export default function guardrail(mathFunction) {
  const queue = [];
  let tmp;
  try {
    tmp = mathFunction();
  } catch (error) {
    tmp = error.toString();
  }
  queue.push(tmp);
  queue.push('Guardrail was processed');
  return queue;
}
