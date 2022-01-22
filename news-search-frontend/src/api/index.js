import axios from "axios";
let host = 'http://gc.caohongchuan.top:8080/';

export const getSearch = (params) => {
    return axios.get(host +`search/querynews?query=${params}`)
}

// export const login = (params) => {
//     return axios.post(host + ``)
// }
//
// export const register = (params) => {
//     return axios.post(host + ``)
// }
//
// export const getRelated = (params) => {
//     return axios.get(host +``)
// }
//
// export const createViewHistory = (params) => {
//     return axios.post(host + ``)
// }
