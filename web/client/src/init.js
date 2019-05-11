(function doodad(){
  var root = document.getElementById('spoil-options')
  var main = document.getElementById('main');

  document.addEventListener('spoil:it', function(){
    main.classList.add('hide');
  });
  document.addEventListener('spoil:back', function(){
    main.classList.remove('hide');
  })
///media/id/spoiler
//http://spoilitfor.me:5000/media
//[{"id":1,"title":"Avengers: Endgame","type":"movie"},{"id":2,"title":"Game of Thrones","type":"tv"}]
  // mock out networking...
  // setTimeout(load, 250);

  fetch('http://spoilitfor.me:5000/media')
    .then(function(res){
      return res.json();
    })
    .then(function(data){
      console.log('data', data);
      load(data);
    });

  function load(data){
    
    root.innerHTML = '';
    data.forEach(function(spoiler){

      var node = document.createElement('div');
      node.classList.add('spoil-option')
      node.innerHTML = spoiler.title;
      node.addEventListener('click', function(evt){
        console.log('clicky', spoiler);
        var spoilEvt = new CustomEvent('spoil:it', {
          detail: {spoiler: spoiler}
        });
        document.dispatchEvent(spoilEvt);
      });
      root.appendChild(node);
    });
  }

})();
