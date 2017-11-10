const URL = 'http://raspberrypi.local:4000';

// Turns the strand off
const off = async function(event) {
  try {
    await axios.get(`/off?animation=${this.offAnimation}`);
  }
  catch (e) {
    console.log(e);
    this.errors.push(e);
  }
}

// Plays strand test of given type
const strandTest = async function(event) {
  try {
    console.log(this);
    this.documents = await axios.get(`/strandtest?animation=${this.strandTestAnimation}`);
  }
  catch (e) {
    console.log(e);
    this.errors.push(e);
  }
}

// Displays a solid color using RGB values
const hue = async function(r, g, b) {
  try {
    await axios.get(`/hue?r=${r}&g=${g}&b=${b}`);
  }
  catch (e) {
    console.log(e);
    this.errors.push(e);
  }
}

// View Model for main app
const appVm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue.js!',
    offAnimation: 'wipe',
    strandTestAnimation: 'rainbowCycle',
    errors: [],
    color_r: 255,
    color_g: 255,
    color_b: 255,
  },
  methods: {
    off,
    strandTest,
    hue,
  },
  created: () => {},
});
