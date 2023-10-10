<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/home';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {

          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<template>
  <form @submit.prevent="submit">
    <input type="email" v-model="form.email" />
    <button type="submit">Submit</button>
  </form>
</template>



<style scoped>
h1,
h3 {
  font-size: 2rem;
}
</style>
