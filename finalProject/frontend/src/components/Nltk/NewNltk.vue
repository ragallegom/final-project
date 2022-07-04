<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Nuevo Corpus</h2>
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
                                    <b-form-select v-model="form.corpus_type" :options="corpus_type"></b-form-select>
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
                                    <b-button type="submit" variant="primary">Crear</b-button>
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
            form: {
                corpus: '',
                description: '',
                corpus_type: 'multiplication'
            },
            corpus_type: [
                { value: 'multiplication', text: 'MULTIPLICATION' },
                { value: 'division', text: 'DIVISION' },
                { value: 'addition', text: 'ADDITION' },
                { value: 'subtraction', text: 'SUBTRACTION' },
                { value: 'equality', text: 'EQUALITY' },
                { value: 'stop_words', text: 'STOP_WORDS' }
            ]
        }
    },
    methods: {
        onSubmit (evt) {
            evt.preventDefault()

            const path = 'http://localhost:8000/api/v1.0/corpus/'

            axios.post(path, this.form).then((response) => {
                this.form.corpus = response.data.corpus
                this.form.description = response.data.description

                swal("Libro creado exitosamente!", "", "success")
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created () {
    }
}
</script>

<style lang="css" scoped>
</style>