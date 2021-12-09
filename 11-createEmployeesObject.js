export default function createEmployeesObject(departmentName, employees) {
  return { [`${departmentName}`]: employees.map((x) => x) };
}
