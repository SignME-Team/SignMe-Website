$(document).on('change', '.file-input', function() {


  var filesCount = $(this)[0].files.length;

  var textbox = $(this).prev();

  if (filesCount === 1) {
    var fileName = $(this).val().split('\\').pop();
    textbox.text(fileName);
  } else {
    textbox.text(filesCount + ' files selected');
  }
});

  function showPreview(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-1-preview");
    preview.src = src;
    console.log("I am here");
    preview.style.display = "block";
  }
}


$(document).ready(function(){
    $('#uploadImage').submit(function(event){
        if($('#uploadFile').val()){
            event.preventDefault();
            $('#loader-icon').show();
            $('#targetLayer').hide();
            $(this).ajaxSubmit({
                target: '#targetLayer',
                beforeSubmit:function(){
                    $('.progress-bar').width('50%');
                },
                uploadProgress: function(event, position, total, percentageComplete)
                {
                    $('.progress-bar').animate({
                        width: percentageComplete + '%'
                    }, {
                        duration: 1000
                    });
                },
                success:function(data){
                    $('#loader-icon').hide();
                    $('#targetLayer').show();
                    $('#targetLayer').append(data.htmlresponse);
                },
                resetForm: true
            });
        }
        return false;
    });
});
