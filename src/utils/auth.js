export function getToken() {
  const token = localStorage.getItem('token');
  return token !== "undefined" ? token : null;
}
  
export function authHeader() {
    const token = getToken();
    return token ? { Authorization: `Bearer ${token}` } : {};
}