$(document).ready(function () {

    const csrftoken = getCookie('csrftoken');


    var table_devices = $('#table-items').DataTable({
        data: [],
        pageLength: 10,
        responsive: false,
        searching: true,
        ordering: true,
        "order": [[ 1, "asc" ]],
        "autoWidth": true,
        fixedColumns: true,
        select: {
            style: 'single'
        },
        dom: '<"html5buttons"B>lTfgitp',
        columns: [
            { "data" : 'id'},
            { "data" : "material_name" },
            { "data" : "quantity" },
            { "data" : "date_required_by" },
            { "data" : "created_at" },
            { "data" : "updated_at" },
        ],
        buttons: [
            {extend: 'copy'},
            {extend: 'csv'},
            {extend: 'excel', title: 'ExampleFile'},
            {extend: 'pdf', title: 'ExampleFile'},

            {extend: 'print',
             customize: function (win){
                    $(win.document.body).addClass('white-bg');
                    $(win.document.body).css('font-size', '10px');

                    $(win.document.body).find('table')
                            .addClass('compact')
                            .css('font-size', 'inherit');
            }
            }
        ],
        "columnDefs": [
                    {
                        render: function( data, type, row, meta) {
                            return `<button class="btn btn-primary btn-sm table-edit-items" type="button" data-id=${data} data-row-index=${meta.row} title="Modifica"><i class="fa fa-edit"></i></button> <button class="btn btn-primary btn-sm table-remove-items" type="button" data-id=${data} title="Cancella" data-toggle="modal"><i class="fa fa-trash"></i></button>`
                        },
                        className: 'text-nowrap',
                        targets: 0,
                        'orderable': false,
                    },
                    {
                        className: 'text-center text-nowrap',
                        targets: [1,2,3],
                    }
                ],

    });

    getTableData()

    function getTableData() {
        $('#myModalloading').modal('show');
        $.ajax({
            url: "/materials/employees_material_requests/employees_material_requests/get",
            type: 'GET',
            headers: { 'X-CSRFToken': csrftoken },
            success: function(res) {
                $('#myModalloading').modal('hide');
                // console.log('load', res)
                tableData = res
                table_devices.rows.add(tableData).draw()
            },
            error : function(xhr,errmsg,err) {
                $('#myModalloading').modal('hide');
                if(xhr.status == 500){
                    var winPrint = window.open();
                    winPrint.document.write(xhr.responseText);
                    winPrint.document.close();
                }
            }
        })
    }


    $(document).on('click','.table-edit-items',function(event){
        $('#myModalloading').modal('show');
        button = this
        row_id = $(button).attr('data-id')

        var modal = $("#modaledit")
        $.ajax({
            url: "/materials/employees_material_requests/employees_material_requests/edit/"+row_id,
            context: document.body,
            error : function(xhr,errmsg,err) {
                $('#myModalloading').modal('hide');
                if(xhr.status == 500){
                    var winPrint = window.open();
                    winPrint.document.write(xhr.responseText);
                    winPrint.document.close();
                }
            }

        }).done(function(response) {
            $('#myModalloading').modal('hide');
            modal.html(response);
            modal.modal('show')
        })
        

    })

     $(document).on('click','.table-remove-items',function(event){
        id = $(this).attr('data-id')

        $("#removeUserModal #removeButton").attr('data-id',id)
        $('#removeUserModal').modal('show')
    })



    $("#removeUserModal #removeButton").click(function(e) {
        $('#myModalloading').modal('show');
        e.preventDefault();
        id = $("#removeUserModal #removeButton").attr('data-id')
        row = $("#table-items .table-edit-items[data-id='"+id+"']").closest('tr')

        rowIndex = table_devices.row(row).index();
        console.log(rowIndex)

        $.ajax({
            url: "/materials/employees_material_requests/employees_material_requests/delete/"+id,
            type: 'GET',
            headers: { 'X-CSRFToken': csrftoken },
            success: function(res) {
                $('#myModalloading').modal('hide')
                table_devices.row(rowIndex).remove().draw()
                $("#delete-successfull").modal('show')
                // close the modal after 1 seconds
                setTimeout(function() {
                    $('#delete-successfull').modal('hide');
                }, 1000);
            },
            error : function(xhr, status, error) {
                console.log(xhr)
                console.log(status)
                console.log(error)
                console.log(xhr.status)
                console.log(xhr.statusText)
                var err  = JSON.parse(xhr.responseText)
                console.log(err)
                $('#myModalloading').modal('hide');
                $("#delete-failed-text").html(err.message);
                $("#delete-failed").modal('show')
                if(xhr.status == 500){
                    var winPrint = window.open();
                    winPrint.document.write(xhr.responseText);
                    winPrint.document.close();
                }

            }
        })

        $('#removeUserModal').modal('hide')
    })


     $(document).on('click','#add-item',function(event){
        $('#myModalloading').modal('show');
        $.ajax({
            url: `/materials/employees_material_requests/employees_material_requests/add`,
            context: document.body,
            error : function(xhr,errmsg,err) {
                $('#myModalloading').modal('hide');
                if(xhr.status == 500){
                    var winPrint = window.open();
                    winPrint.document.write(xhr.responseText);
                    winPrint.document.close();
                }
            }
        }).done(function(response) {
            $('#myModalloading').modal('hide');
            $("#modaladd").html(response);
            $('#modaladd').modal('show')
        });
    })

    $('#modaladd').on('hidden.bs.modal', function () {
        $('#modaladd').empty();
    });


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }   


})