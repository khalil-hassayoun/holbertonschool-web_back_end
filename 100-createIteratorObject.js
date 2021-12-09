export default function createIteratorObject(report) {
  const emp = [];
  for (const k of Object.keys(report.allEmployees)) {
    emp.push(...report.allEmployees[k]);
  }
  return emp;
}
