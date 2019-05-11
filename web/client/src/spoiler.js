(function(){
  console.log('spoiler!');
  var spoiledRoot = document.getElementById('spoiled');
  var backBtn = document.getElementById('back-btn');
  var againBtn = document.getElementById('again-btn');
  var spoiler = document.getElementById('spoiler');
  var spoilerNode = document.getElementById('text');
  
  var lastData = undefined;

  document.addEventListener('spoil:it', function(data){
    spoiledRoot.classList.add('show');
    console.log('spoiler data', data);
    lastData = data;

    fetch(`http://spoilitfor.me:5000/media/${data.id}/spoiler`)
      .then(function(res){
        return res.json();
      })
      .then(function(data){
        spoiler.classList.add('show');
        spoilerNode.innerHTML = data.message;
        console.log('spoiler', data);
      });
  
  });

  document.addEventListener('spoil:back', function(){
    spoiledRoot.classList.remove('show');
    spoiler.classList.remove('show');
  });

  backBtn.addEventListener('click', function(){
    var backEvt = new CustomEvent('spoil:back');
    document.dispatchEvent(backEvt);
  })

  againBtn.addEventListener('click', function(){
    spoiler.classList.remove('show');
    setTimeout(function(){

      var spoilEvt = new CustomEvent('spoil:it', {
        spoiler: lastData
      });
      document.dispatchEvent(spoilEvt);
    }, 300)

  });

})();