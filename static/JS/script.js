//ShareButton
const ShareButton = document.querySelectorAll('#shareButton');
const overlay = document.querySelector('.overlay');
const members = document.querySelector('.members');
const favourite = document.querySelectorAll('#fbutton')
const left = document.querySelectorAll('#left');
const right = document.querySelectorAll('#right');

for(let i = 0;i<left.length;i++){
right[i].addEventListener('click',(e)=>{
    e.target.parentElement.getElementsByTagName('div')[1].scrollLeft+=80;
    e.target.parentElement.getElementsByTagName('div')[1].style.scrollBehaviour = 'smooth'

})
left[i].addEventListener('click',(e)=>{
    e.target.parentElement.getElementsByTagName('div')[1].scrollLeft-=80;
    e.target.parentElement.getElementsByTagName('div')[1].style.scrollBehaviour = 'smooth'

})
}

//click Event Listener add to the share button
for(let i =0;i<favourite.length;i++){
    favourite[i].addEventListener('click',(e)=>{
        fetch(`http://127.0.0.1:8000/AddFavourite/${e.srcElement.ariaValueText}`)
        console.log(e.srcElement.ariaValueText)
        if(favourite[i].className === "fa fa-heart"){
            favourite[i].className="fa fa-heart-o";
            favourite[i].style.color="white";
        }
        else{
            favourite[i].className="fa fa-heart"
            favourite[i].style.color="red"
        }
        window.location.href = '/';
    })
}


overlay.addEventListener('click',()=>{
    
    members.style.display="none";
})


// camera
let stream
let camera_button = document.querySelector("#start-camera");
let camera_close = document.querySelector("#close-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let crd = document.querySelector('.crd');
let cx = document.querySelector('.cx');

camera_button.addEventListener("click", async function () {
  stream = await navigator.mediaDevices.getUserMedia({
    video: true,
    audio: false,
  });
  camera_button.style.display="none"
  camera_close.style.display="block"
  cx.style.display="block";
  crd.style.display="block";
  crd.style.opacity="1"
  video.srcObject = stream;
  overlay.style.display="block";
});
camera_close.addEventListener("click", function () {
    if (stream) {
        let tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
      }
    camera_button.style.display="block"
  camera_close.style.display="none"
  cx.style.display="none";
  crd.style.display="none";
  overlay.style.display="none";
} )

click_button.addEventListener("click", function () {
   
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
  let image_data_url = canvas.toDataURL("image/jpeg");

  // data url of the image
  
  fetch('http://127.0.0.1:8000/predict_emotion/', {
    method: 'POST',
    
    headers: {
        'Content-Type': 'application/json',
        
    },
    
    body: JSON.stringify({ image_data: image_data_url }),
   

})

.then(response => response.json())
.then(data => {
    // Handle the response from the Django app
    console.log(data);
    window.location.href = '/songs/' + data.emotion;

})
.catch(err =>{
    console.log(err)
})
});


