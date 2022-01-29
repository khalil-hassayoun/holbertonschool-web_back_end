import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignUp(firstName, lastName, fileName) {
  const stats = [];
  await signUpUser(firstName, lastName)
    .then(async (data) => {
      stats.push({
        status: 'fulfilled',
        value: data,
      });
      await uploadPhoto(fileName);
    })
    .catch((err) => {
      stats.push({
        status: 'rejected',
        value: err.toString(),
      });
    });
  return stats;
}
