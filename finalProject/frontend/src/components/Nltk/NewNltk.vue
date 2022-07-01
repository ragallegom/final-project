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
                description: ''
            }
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