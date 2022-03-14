import axios from "axios";

let host_1 = 'http://gc.caohongchuan.top:8080';
// let host_2 = 'http://gc.caohongchuan.top:7788/';

export const getSearch = (params, pageNum, pageSize) => {
    return axios.get(host_1 + `/search/querynews?query=${params}&page=${pageNum}&pagesize=${pageSize}`);
}
export const updateRecords = (params) => {
    return axios.put(host_1 + `/search/viewrecord`, params)
}

export const register = (params) => {
    return axios.post(host_1 + `/login/register`, params)
}

export const login = (params) => {
    return axios.post(host_1 + `/recommend/renews`, params)
}

export const updateRecommends = () => {
    return axios.get(host_1 + `/recommend/update`)
}
export const getAllCountries = () => {
    return axios.get(host_1 + `/search/getcountry`)
}
export const getAllThemeCountries = () => {
    return axios.get(host_1 + `/search/getcountytheme`)
}
export const getAllTheme = () => {
    return axios.get(host_1 + `/search/gettheme`)
}
export const getNewsByTheme = (params, pageNum, pageSize) => {
    return axios.get(host_1 + `/search/newsbytheme?theme=${params}&page=${pageNum}&pagesize=${pageSize}`)
}
export const getNewsByCountry = (params, pageNum, pageSize) => {
    return axios.get(host_1 + `/search/newsbycountry?country=${params}&page=${pageNum}&pagesize=${pageSize}`)
}

export const getNewsByTime = (startTime, endTime, pageNum, pageSize) => {
    return axios.get(host_1 + `/search/newsbytime?starttime=${startTime}&endtime=${endTime}&page=${pageNum}&pagesize=${pageSize}`);
}

export const getWordCorrection = (param) => {
    return axios.get(host_1 + `/search/wordsug?wordsug=${param}`);
}
