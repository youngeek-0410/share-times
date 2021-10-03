type Token = string
type bodyData =  {
    username: string
    password: string
}

const login = async (username: string, password: string) => {
    const body: bodyData = {
        username: username,
        password: password
    }
    
    fetch("http://localhost/api-token-auth/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
    .then(res => res.json())
    .then((data: {'token': Token}) => {
        localStorage.setItem('token', data.token)
    }) 
    .catch(error => {
        console.log(error)
    })
}

export default login