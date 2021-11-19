<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit User Profile</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form
            v-model="valid"
            ref="form"
            lazy-validation
          >
            <v-text-field
              label="Nombre(s)"
              v-model="first_name"
              required
            ></v-text-field>
            <v-text-field
              label="Apellido(s)"
              v-model="last_name"
              required
            ></v-text-field>
            <v-text-field
              label="E-mail"
              type="email"
              v-model="email"
              v-validate="'required|email'"
              data-vv-name="email"
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
            <v-text-field
              label="Género"
              v-model="gender"
              required
            ></v-text-field>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn
          @click="submit"
          :disabled="!valid"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfileUpdate } from '@/interfaces';
import { readUserProfile } from '@/store/main/getters';
import { dispatchUpdateUserProfile } from '@/store/main/actions';

@Component
export default class UserProfileEdit extends Vue {
  public valid = true;
  public first_name: string = '';
  public last_name: string = '';
  public email: string = '';
  public gender: string = '';

  public created() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.first_name = userProfile.first_name;
      this.last_name = userProfile.last_name;
      this.email = userProfile.email;
      this.gender = userProfile.gender;
    }
  }

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public reset() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.first_name = userProfile.first_name;
      this.last_name = userProfile.last_name;
      this.email = userProfile.email;
      this.gender = userProfile.gender;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if ((this.$refs.form as any).validate()) {
      const updatedProfile: IUserProfileUpdate = {};
      if (this.first_name) {
        updatedProfile.first_name = this.first_name;
      }
      if (this.last_name) {
        updatedProfile.last_name = this.last_name;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      if (this.gender) {
        updatedProfile.gender = this.gender;
      }
      await dispatchUpdateUserProfile(this.$store, updatedProfile);
      this.$router.push('/main/profile');
    }
  }
}
</script>
