$(function () {
  const addDiv = $('#add_item');
  const removeDiv = $('#remove_item');
  const clearDiv = $('#clear_list');
  const ulList = $('ul.my_list');

  addDiv.bind('click', function () {
    ulList.append($('<li></li>').text('Item'));
  });

  removeDiv.bind('click', function () {
    $('ul.my_list li:last').remove();
  });

  clearDiv.bind('click', function () {
    ulList.empty();
  });
});
