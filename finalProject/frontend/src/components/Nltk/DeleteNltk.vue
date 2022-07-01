<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>¿Estas seguro que deseas eliminar este libro?</h3>
                <p>Corpus : {{ this.element.corpus }}</p>
                <p>Descripción : {{ this.element.description }}</p>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <b-button v-on:click="deleteCorpus" variant="danger">Eliminar</b-button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

export default {
    data () {
        return {
            corpusId: this.$route.params.corpusId,
            element: {
                corpus: '',
                description: ''
            }
        }
    },
    methods: {
        getCorpus () {
            const path = `http://localhost:8000/api/v1.0/corpus/${this.corpusId}/`

            axios.get(path).then((response) => {
                this.element.corpus = response.data.corpus
                this.element.description = response.data.description
            })
            .catch((error) => {
                console.log(error)
            })
        },
        deleteCorpus () {
            const path = `http://localhost:8000/api/v1.0/corpus/${this.corpusId}/`

            axios.delete(path).then((response) => {
                location.href = '/corpus'
            })
            .catch((error) => {
                swal("No es posible eliminar el libro", "", "error")
            })
        }
    },
    created () {
        this.getCorpus()
    }
}
</script>

<style lang="css" scoped>
</style>