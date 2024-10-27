import React, { useState } from 'react'

/*
<img id="logo" src="/static/images/logo.png">
<br>
<form action="prompt" method="post">
    <p>What kind of image would you like to generate?</p>
    <br>
    <input id="prompt" type="text" name="prompt_input">
    <br>
    <input id="generate_btn" type="submit" value="GENERATE" onclick="processing();">
</form>
<form action="supersample" method="post">
    {% for i in prompt_images %}
        <img class="generated" src="{{i}}">
    {% endfor %}
    <br>
    {% for i in btn_range %}
    <button class="save_btn" name="save_btn" type="submit" value="{{i}}" onclick="saving({{i}});">
    SAVE HD IMAGE
    </button>
    {% endfor %}
</form>
*/

const APIURL = "http://127.0.0.1:11437"




const ImgGen = () => {

    const [images, setImages] = useState<any[]>([])
    const saveImages = (imagePath:string) => {
        //fetch(APIURL, )
        console.log("Image saved", imagePath)
    }



    const generateImages = (formElement:React.FormEvent<HTMLFormElement>) => {
        formElement.preventDefault();

        console.log(formElement)
        const prompt = formElement.target.prompt.value
        console.log(prompt, "HAASDFASDF")
        const requestOptions = {
            method: 'POST',
            body: JSON.stringify({ prompt: prompt })
        };
        

        const getShit = async () => {
            const response = await fetch(
                `${APIURL}/prompt`,
                requestOptions
            ).then((r)=> r ).catch((error)=>console.error(error));
            if (!response || !response.ok) {
                console.error("This shit failed")
            } else {
                console.log("SUCCESS", await response.json())
            }
        }
        getShit();

    }

    return (
        <>
            <div>
                <form onSubmit={generateImages}>
                    <p>What kind of image would you like to generate?</p>
                    <br/>
                    <input id="prompt" type="text" name="prompt_input"/>
                    <br/>
                    <input type="submit"/>
                </form>
                <form action={`${APIURL}/supersample`} method="post">
                {
                    images.map((img)=>{
                        return (
                        <>
                            <img src={`${APIURL}/${img}`} alt='This is img' />
                            <button className="saveButton" value={img}>
                                SAVE HD IMAGE
                            </button>
                        </>
                        )
                    })

                }

                </form>
            </div>
        </>
    )
}

export default ImgGen;
