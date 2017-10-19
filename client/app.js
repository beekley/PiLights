const URL = 'http://raspberrypi.local:4000';

// Retrieves all documents
// const getDocuments = async function() {
//   try {
//     console.log(this);
//     this.documents = await axios.get(`${URL}/api/document`);
//   }
//   catch (e) {
//     this.errors.push(e);
//   }
// }

// View Model for main app
const appVm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!',
    documents: [],
    errors: [],
  },
  methods: {
  },
  created: () => {},
});
