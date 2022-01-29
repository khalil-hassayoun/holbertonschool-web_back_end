export default function getStudentIdsSum(students) {
  if (Array.isArray(students)) return students.reduce((acc, stud) => acc + stud.id, 0);
  return 0;
}
