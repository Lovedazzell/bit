let data_show = document.getElementById('progress-bar-message')
let data = document.getElementById('progress-bar-message').innerText
console.log(data_show)
console.log(data)

if(data_show.innerText == 'Waiting for progress to start...'){
    console.log('watting ,data is  need to hide')
}

if(data_show.innerText ==  'Task started...'){
    console.log('task started , data is  need to hide')
}

if(data.slice(0,7) ==  'Success!'){
    console.log('Success , data is  need to hide')
}
