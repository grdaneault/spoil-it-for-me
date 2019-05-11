(function doodad(){
  console.log('hello world');
  var root = document.getElementById('spoil-options')
  console.log(root)


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
      console.log(spoiler);

      var node = document.createElement('div');
      node.classList.add('spoil-option')
      node.innerHTML = spoiler;
      node.addEventListener('click', function(evt){
        console.log('clicky', spoiler)
      });
      root.appendChild(node);
    });
  }

})();
