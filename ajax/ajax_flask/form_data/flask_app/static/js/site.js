
function getUsers(){
    fetch('http://localhost:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            users.innerHTML = "";
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();


window.onload = (e) => {

    var createUser = document.getElementById('createUser');
    createUser.onsubmit = function(e){
        e.preventDefault();
        var form = new FormData(createUser);
        fetch("http://localhost:5000/create/user", {method : 'POST', body : form})
            .then(response => response.json)
            .then(data => console.log(data))

        getUsers();
        createUser.reset();
    }
    
}