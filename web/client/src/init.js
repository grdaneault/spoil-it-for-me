(function doodad(){
  var root = document.getElementById('spoil-options')
  var main = document.getElementById('main');

  document.addEventListener('spoil:it', function(){
    main.classList.add('hide');
  });
  document.addEventListener('spoil:back', function(){
    main.classList.remove('hide');
  })


  // mock out networking...
  setTimeout(load, 250);

  function load(){
    var spoilers = [
      'Game of Thrones',
      'Harry Potter',
      'Avengers',
      'Mr. Robot'
    ]
    root.innerHTML = '';
    spoilers.forEach(function(spoiler){

      var node = document.createElement('div');
      node.classList.add('spoil-option')
      node.innerHTML = spoiler;
      node.addEventListener('click', function(evt){
        console.log('clicky', spoiler);
        var spoilEvt = new CustomEvent('spoil:it', {
          show: spoiler
        });
        document.dispatchEvent(spoilEvt);
      });
      root.appendChild(node);
    });
  }

})();
