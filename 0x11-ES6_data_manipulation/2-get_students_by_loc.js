export default function getStudentsByLocation(students, filter) {
  if (Array.isArray(students)) return students.filter((student) => student.location === filter);
  return [];
}
