(function(){
  console.log('spoiler!');
  var spoiledRoot = document.getElementById('spoiled');
  var backBtn = document.getElementById('back-btn');
  var spoiler = document.getElementById('spoiler');
  
  
  document.addEventListener('spoil:it', function(){
    spoiledRoot.classList.add('show');

    setTimeout(function(){
      spoiler.classList.add('show');
    }, 600);

  });

  document.addEventListener('spoil:back', function(){
    spoiledRoot.classList.remove('show');
  });

  backBtn.addEventListener('click', function(){
    var backEvt = new CustomEvent('spoil:back');
    document.dispatchEvent(backEvt);
  })

})();