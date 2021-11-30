// var url = 'http://127.0.0.1:5000/job_listings_get_api';
var url = 'http://time.jsontest.com/';

$.ajax({
  url: url,
  method: 'GET',
}).done(function(result) {
  // JSON data array
  var data = result.surrey;

  // get DOM node to be parent of child list nodes
  var $data = $('#data');

  // iterate through each object in JSON array
  data.forEach(function(item) {

    // create an unordered list node
    var $ul = $('<ul></ul>');

    // iterate through all the properties of current JSON object
    for (var field in item) {

      // append list item node to list node
      $ul.append(`<li>${field}: ${item[field]}</li>`);
    }

    // append list node to parent node
    $data.append($ul);
  });
}).fail(function(error) {
  console.error(error);
});

// $(document).ready(function(){
//     $(".flip").click(function(){
//       $(".panel").slideDown("slow");
//     });
//   });