console.log("Assest file working");
const API = {
    errHandler: () => {},
    get: async (url, data = {}) => {
        return await $.ajax({
            type: "GET",
            url: url,
            data: data,
            success: (data) => {
                if (data?.success) return data;
                // error handler
                API.errHandler();
            },
        });
    },
    post: async (url, data = {}) => {
        return await $.ajax({
            type: "POST",
            url: url,
            // headers: {
            //     "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val(),
            // },
            data: data,
            success: (data) => {
                if (data?.success) return data;
                // error handler
                API.errHandler();
            },
        });
    },
};

const APIROUTES = {
    get: {
        index: "/",
    },
    post: {
        default: "ajax/",
    },
};

const Ajax = async () => {
    let data = await API.post(APIROUTES.post.default, {});
    console.log(data);
};
