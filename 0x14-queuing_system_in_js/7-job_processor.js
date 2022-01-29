import kue from 'kue';
const queue = kue.createQueue();

const blacklistedPhoneNumbers = [
  '4153518780', '4153518781'
];

const sendNotification = (phoneNumber, message, job, done) => {
  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.process(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.phoneNumber, job.message, job, done);
  done();
});
