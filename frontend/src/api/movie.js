import Vue from 'vue';

class MovieAPI {
    getMovie = (params) => Vue.prototype.$axios.get("http://localhost:8000/api/Movies/" + params);
}

export default new MovieAPI();