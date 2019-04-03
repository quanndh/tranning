let songContainer = document.getElementById('song_container')
let song = songContainer.getElementsByClassName('song')
let x = song[0].getElementsByClassName('title').innerText;

for(let i = 0; i < song.length; i++){
    console.log(song[i])
    console.log(song[i].getElementsByClassName('title')[0].innerText)
    console.log(song[i].getElementsByClassName('artist')[0].innerText)
}

song[0].getElementsByTagName('i')[0].addEventListener('click', () => {
    song[0].innerHTML = '' 
})
song[1].getElementsByTagName('i')[0].addEventListener('click', () => {
    song[1].innerHTML = '' 
})
song[2].getElementsByTagName('i')[0].addEventListener('click', () => {
    song[2].innerHTML = '' 
})

song[0].getElementsByTagName('i')[1].addEventListener('click', () => {
    console.log(song[0].getAttribute('song_id')) 
})
song[1].getElementsByTagName('i')[1].addEventListener('click', () => {
    console.log(song[1].getAttribute('song_id')) 
})
song[2].getElementsByTagName('i')[1].addEventListener('click', () => {
    console.log(song[2].getAttribute('song_id')) 
})

song[0].getElementsByTagName('i')[2].addEventListener('click', () => {
    console.log(song[0].getAttribute('song_id') + " name: " + song[0].getElementsByClassName('title')[0].innerText + ", artist: " + song[0].getElementsByClassName('artist')[0].innerText) 
})
song[1].getElementsByTagName('i')[2].addEventListener('click', () => {
    console.log(song[1].getAttribute('song_id') + " name: " + song[1].getElementsByClassName('title')[0].innerText + ", artist: " + song[1].getElementsByClassName('artist')[0].innerText) 
})
song[2].getElementsByTagName('i')[2].addEventListener('click', () => {
    console.log(song[2].getAttribute('song_id') + " name: " + song[2].getElementsByClassName('title')[0].innerText + ", artist: " + song[2].getElementsByClassName('artist')[0].innerText) 
})

let btn = document.getElementById('btn')
btn.addEventListener('click', () => {
    $("#song_container").append(`
        <hr>
        <div class="song" song_id="12354">
            <h4 class="title">Whatever it takes</h4>
            <h5 class="artist">Imagine Dragons</h5>
            <i>Delete</i>
            <i>Edit</i>
            <i>More</i>
        </div>
    `)
})

