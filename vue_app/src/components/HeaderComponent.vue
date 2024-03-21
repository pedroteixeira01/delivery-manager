<template>
    <header>
        <div id="logo">
            <h2>
                Delivery Manager
            </h2>
        </div>

        <nav>
            <router-link to="/">Home</router-link>
            <router-link to="/trucks">Trucks</router-link>
            <router-link to="/cargos">Cargos</router-link>
        </nav>
    </header>
</template>

<script>
export default {
    name: 'HeaderComponent',
}
</script>

<style scoped>
header{
    background-color: #404040;
    display: flex;
}

#logo{
    padding-top: 27px;
    padding-bottom: 15px;
    margin-left: 69px;
    flex: 2;
}

#logo h2{
    color: white;
    font-size: 40px;
    width: 100px;
}

nav{
    flex: 1;
    color: white;
    font-size: 35px;
    display: flex;
    gap: 20px;
    padding-top: 46px;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>