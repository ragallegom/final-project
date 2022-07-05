<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col-sm-8 text-left">
                <h2>Editar Corpus</h2>
            </div>
            <div class="col-sm-4">
                <b-button to="/" squared variant="primary">Inicio</b-button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="corpus" class="col-sm-2 col-form-label">Tipo</label>
                                <div class="col-sm-6">
                                    <input type="text" name="corpus_type" class="form-control" v-model.trim="form.corpus_type" disabled></input>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="corpus" class="col-sm-2 col-form-label">Corpus</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Corpus" name="corpus" class="form-control" v-model.trim="form.corpus"></input>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.description""></textarea>
                                </div>
                            </div>
                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Editar</b-button>
                                    <b-button type="submit" class="btn-large-space" :to="{ name: 'ListNltk'}">Cancelar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data () {
        return {
            corpusId: this.$route.params.corpusId,
            form: {
                corpus_type: '',
                corpus: '',
                description: ''
            }
        }
    },
    methods: {
        onSubmit (evt) {
            evt.preventDefault()

            const path = `http://localhost:8000/api/v1.0/corpus/${this.corpusId}/`

            axios.put(path, this.form).then((response) => {
                this.form.corpus = response.data.corpus
                this.form.description = response.data.description
                this.form.corpus_type = response.data.corpus_type

                swal("Libro actualizado exitosamente!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })
        },

        getCorpus () {
            const path = `http://localhost:8000/api/v1.0/corpus/${this.corpusId}/`

            axios.get(path).then((response) => {
                this.form.corpus = response.data.corpus
                this.form.description = response.data.description
                this.form.corpus_type = response.data.corpus_type
            })
            .catch((error) => {
                console.log(error)
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