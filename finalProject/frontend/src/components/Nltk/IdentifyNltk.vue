<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Identificar</h2>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Texto en inglés</label>
                                <div class="col-sm-6">
                                    <textarea name="corpus" class="form-control" placeholder="..." rows="3"
                                        v-model.trim="form.corpus"></textarea>
                                </div>
                            </div>
                            <div class=" rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Identificar</b-button>
                                    <b-button @click="resetResult" variant="danger">Limpiar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Tokenización - Oraciones"
                    header-tag="header"
                    footer="Al tokenizar, se puede dividir convenientemente el texto por palabras o por oraciones. Esto le permitirá trabajar con fragmentos de texto más pequeños que aún son coherentes y significativos, incluso fuera del contexto del resto del texto"
                    footer-tag="footer"
                    footer-bg-variant="secondary"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="sentence in sent_tokenize">{{ sentence }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Tokenización - Palabras"
                    header-tag="header"
                    footer="La tokenización por palabras, nos permite dividir por palabras que son como los átomos del lenguaje natural. Son la unidad de significado más pequeña que todavía tiene sentido por sí misma"
                    footer-tag="footer"
                    footer-bg-variant="secondary"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="word in word_tokenize">{{ word }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Stopwords - Palabras vacías"
                    header-tag="header"
                    footer="Las palabras vacías son palabras que desea ignorar, por lo que se filtran del texto cuando este es procesado. Palabras muy comunes como ‘en’, ‘es’ y ‘un’ a menudo se usan como palabras vacías, ya que no agregan significado a un texto por sí mismas"
                    footer-tag="footer"
                    footer-bg-variant="secondary"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="word in stopwords">{{ word }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Lemmatization"
                    header-tag="header"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="word in stopwords">{{ word }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Equations"
                    header-tag="header"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="word in equations">{{ word }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col">
                <b-card
                    header="Binary Expression Tree"
                    header-tag="header"
                    border-variant="dark"
                    v-if="showResult"
                    >
                    <b-card-text>
                        <b-list-group>
                            <b-list-group-item v-for="word in binaryExpTree">{{ word }}</b-list-group-item>
                        </b-list-group>
                    </b-card-text>
                </b-card>
            </div>
        </div>
        <br>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data() {
        return {
            form: {
                corpus: '',
                description: ''
            },
            showResult: false,
            sent_tokenize: [],
            word_tokenize: [],
            stopwords: [],
            lemmatization: [],
            equations: [],
            binaryExpTree: [],
        }
    },
    methods: {
        onSubmit(evt) {
            evt.preventDefault()
            this.resetResult()

            const path = 'http://localhost:8000/api/v1.0/identify/'

            axios.post(path, this.form).then((response) => {

                this.showResult = true
                this.sent_tokenize = response.data['sentences']
                this.word_tokenize = response.data['words']
                this.stopwords = response.data['stopwords']
                this.lemmatization = response.data['lemmatization']
                this.equations = response.data['equations']
                this.binaryExpTree = response.data['binaryExpTree']

                swal("Texto identificado correctamente!", "", "success")
            })
            .catch((error) => {
                swal("Error al identificar!", "", "error")
            })
        },
        resetResult (evt) {
            this.showResult = false
        }
    },
    created() {
    }
}
</script>

<style lang="css" scoped>
</style>