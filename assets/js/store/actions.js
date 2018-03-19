import axios from 'axios';

export default {
  login(context, { username, password }) {
    axios.post('api/token-auth/', { username, password })
      .then(response => context.commit('loginSuccess', response.data.token));
  }
}
