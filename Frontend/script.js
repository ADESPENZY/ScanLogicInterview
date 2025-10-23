const BASE_URL = "http://127.0.0.1:8000/api/";

    $("#fetch").click(() => {
      const name = $("#name").val();
      if (!name) return $("#msg").text("Enter a name first.");

      $.ajax({
        url: BASE_URL + "getProfile/",
        type: "GET",
        data: { name },
        success: (res) => {
          $("#email").val(res.email);
          $("#phone").val(res.phone);
          $("#msg").text("Record found.");
        },
        error: () => {
          $("#email").val("");
          $("#phone").val("");
          $("#msg").text("No record found.");
        },
      });
    });

    $("#save").click(() => {
      const data = {
        name: $("#name").val(),
        email: $("#email").val(),
        phone: $("#phone").val(),
      };

      $.ajax({
        url: BASE_URL + "saveProfile/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: (res) => $("#msg").text(res.message),
        error: () => $("#msg").text("Error saving record."),
      });
    });