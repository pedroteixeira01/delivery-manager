<template>
    <div>  
        <h1>
            Tools
        </h1>

        <div id="tools">
            <h2>Get the best truck for a cargo</h2>
            <button id="bestBtn" @click="$router.push('/mapping')">
                Try Now
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeView',
}
</script>

<style scoped>
h1{
    font-size: 50px;
    margin-top: 40px;
    margin-left: 67px;
    margin-bottom: 30px;
}

#tools{
    background-color: #404040;
    border-radius: 10px;
    width: 70%;
    height: auto;
    margin-left: 15%;
}

h2{
    color: white;
    margin-left: 40px;
    padding-top: 20px;
}

#bestBtn{
    background-color: #42b983;
    border: none;
    border-radius: 10%;
    padding: 10px;
    font-size: 20px;
    margin-left: 40px;
    margin-top: 20px;
    margin-bottom: 10px;
}

#bestBtn:hover{
    background-color: #187a4e;
    cursor: pointer;
}

</style>