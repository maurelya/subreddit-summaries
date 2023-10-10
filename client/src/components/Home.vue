<template>
  <div>
    <h1>Welcome to the subreddit summarizer</h1>
    <p>The subreddit summarizer will sent you daily emails of your favorite subreddit.
      The emails will contain the top post of the subreddit with a brief summary of the top comments.
    </p>
    <p>Please fill and submit the form below to start getting daily emails.</p>
  </div>
  <div>
    <form @submit.prevent="submitForm" v-if="!formSubmitted">
      <span>Enter your name</span><br>
      <input v-model="name" type="text" placeholder="Enter your name" /><br>

      <span>Enter your email</span><br>
      <input v-model="email" type="email" placeholder="Enter your email" /><br>

      <span>Enter the subreddit</span><br>
      <input v-model="subreddit" type="subreddit" placeholder="Enter the subreddit" /><br>

      <input class="submit" type="submit" value="Submit">
    </form>
    <div v-if="formSubmitted">
      <h3>Form Submitted</h3>
      <p>Name: {{ name }}</p>
      <p>Email: {{ email }}</p>
      <p>Subreddit: {{ subreddit }}</p>
      <small>Click on run to launch the app again.</small>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      subreddit: "",
      formSubmitted: false
    };
  },
  methods: {
    submitForm: function () {
      this.formSubmitted = true
      axios.post('/submit', form.data)
        .then((response) => {
          // Success
        })
        .catch((error) => {
          // Error
        });
    }
  },
};
</script>
<style>
p,
h1 {
  /* Center horizontally*/
  text-align: left;

}

form {
  padding: 10px;
  border: 2px solid black;
  border-radius: 5px;
}

input {
  padding: 4px 8px;
  margin: 4px;
}

span {
  font-size: 18px;
  margin: 4px;
  font-weight: 500;
}

.submit {
  font-size: 15px;
  color: #fff;
  background: #222;
  padding: 6px 12px;
  border: none;
  margin-top: 8px;
  cursor: pointer;
  border-radius: 5px;
}
</style>