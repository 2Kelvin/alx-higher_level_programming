$(function () {
  const clickDiv = $('#add_item');
  const ulList = $('ul.my_list');

  clickDiv.bind('click', function () {
    ulList.append($('<li></li>').text('Item'));
  });
});
