<!--
<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                Crear encuesta
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field label="Título" v-model="title" required/>
                        <v-textarea label="Descripción" v-model="description" required/>
                        <v-checkbox label="Esta activa" v-model="isActive"/>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancelar</v-btn>
                <v-btn @click="reset">Restablecer</v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Guardar
                    </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue} from 'vue-property-decorator';
import IUSurveyCreate from '@interfaces';
import { readUserProfile } from '@/store/main/getters';

@Component
export default class CreateSurvey extends Vue {
    public valid = false;
    public title: string = "";
    public description: string = "";
    public isActive: boolean = true;

    public async mounted() {
        // await
        this.reset();
    }

    public reset() {
        this.title = '';
        this.description = '';
        this.isActive = true;
        this.$validator.reset();
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const createSurvey: IUSurveyCreate = {
                title: this.title
            };
            if (this.description) {
                createSurvey.description = this.description;
            }
            createSurvey.active_survey = this.isActive;

            await 
            this.$router.push('/main/survey/all')
        }
    }
}
</script>
-->
