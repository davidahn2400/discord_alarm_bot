const axios = require("axios");

exports.handler = async (event) => {

    try{
        const result = await axios.post("https://discord.com/api/webhooks/1192443373076893706/WL-sMxnRYb3cms8QQHJYBEBPebiVVm-yco2v9dNSVq5nNs0gcDT6aDjO4oXBxX75Y_1z", {
            "content" : "떠상 알리미 테스트중!"
        });
        console.info("디스코드 웹훅 성공");
    }
    catch(erR){
        console.err("디스코드 웹훅 실패", err);
    }


    const response = {
        statusCode : 200,
        body : JSON.stringify('Hello from Lambda!'),
    };
    return response;
};