<template lang="html">
    <div>
        <b-jumbotron>
            <template #header>Lingüística computacional</template>

            <template #lead>
                Sistema de Software en Python con librerías NLTK
                (Natural Language Tool Kit) para identificar en un texto en inglés un
                elemento (ecuación) y lo
                traduzca en lenguaje controlado.
            </template>

            <hr class="my-4">

            <p>
                Jorge Luis Higuita - Rodrigo Andrés Gallego
            </p>

            <b-button variant="primary" :to="{ name: 'IdentifyNltk'}">Identicar</b-button>
            <b-button variant="success" :to="{ name: 'ListNltk'}">Corpus</b-button>
        </b-jumbotron>
    </div>
</template>

<script>

export default {
    data() {
        return {
        }
    },
    methods: {
    },
    created() {
    }
}
</script>

<style lang="css" scoped>
</style>