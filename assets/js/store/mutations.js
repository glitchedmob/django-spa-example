import axios from 'axios';

export default {
  loginSuccess(state, payload) {
    state.loggedIn = true;
    state.token = payload;
    axios.defaults.headers.common['Authorization'] = `Bearer ${state.token}`;
  },
  logout(state) {
    state.loggedIn = false;
    state.token = false;
    axios.defaults.headers.common['Authorization'] = '';
  }
}
