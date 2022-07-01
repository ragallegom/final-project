<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div>
                    <h2>Listado del Corpus</h2>
                    <b-button size="sm" :to="{ name:'NewNltk' }" variant="primary">
                        Nuevo corpus
                    </b-button>
                </div>
                <br>
                <div class="col-md-12">
                    <b-table striped hover :items="corpus" :fields="fields">
                        <template #cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{ name:'EditNltk', params: {corpusId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger"  :to="{ name:'DeleteNltk', params: {corpusId: data.item.id}}">
                                Eliminar
                            </b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            fields: [
                { key: 'corpus', label: 'Corpus' },
                { key: 'description', label: 'Descripción' },
                { key: 'action', label: '' },
            ],
            corpus: []
        }
    },
    methods: {
        getCorpus() {
            const path = 'http://localhost:8000/api/v1.0/corpus/'
            axios.get(path).then((response) => {
                this.corpus = response.data
            })
                .catch((error) => {
                    console.log(error)
                })
        }
    },
    created() {
        this.getCorpus()
    }
}
</script>

<style lang="css" scoped>
</style>