import axios from 'axios'
/* eslint-disable no-undef */

import applyCaseMiddleware from 'axios-case-converter'

const getToken = () => window.localStorage.getItem('accessToken')

const backendUrl = process.env.NODE_ENV === 'development' ? 'http://localhost:8000' : 'http://managr.telebox.it:8000'

const axiosInstance = applyCaseMiddleware(
  axios.create({
    baseURL: backendUrl
  })
)

axiosInstance.interceptors.request.use(config => {
  const accessToken = getToken()
  if (accessToken) {
    config.headers.Authorization = accessToken
  }

  return config
})

export default axiosInstance
