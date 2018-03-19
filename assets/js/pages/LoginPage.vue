<template>
	<div class="container">
		<b-card
			@submit="submit"
			title="Login"
			tag="section"
			class="ma-2">
			<b-form>
				<b-form-group
					label="Username:"
					label-for="username">
					<b-form-input
						v-model="form.username"
						id="username"
						type="text"
						required
						placeholder="Enter username">
					</b-form-input>
				</b-form-group>
				<b-form-group
					label="Password"
					label-for="password">
					<b-form-input
						v-model="form.password"
						id="password"
						type="password"
						required
						placeholder="Enter password">
					</b-form-input>
				</b-form-group>
				<b-button type="submit" variant="primary">Login</b-button>
			</b-form>
		</b-card>
	</div>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";

export default {
	data: () => ({
		form: {
			username: '',
			password: ''
		}
	}),
  computed: {
    ...mapState(['loggedIn'])
	},
	created() {
		if (this.loggedIn) {
			this.$router.push({ name: 'all-posts' })
		}
	},
	methods: {
		...mapActions(['login']),
		submit(e) {
			e.preventDefault();
			this.login(this.form);
			this.$router.push({ name: 'all-posts' })
		}
	}
};
</script>

<style lang="scss" scoped>
	.container {
		min-height: calc(100vh - 56px);
		display: flex;
		align-items: center;
		align-content: center;

		> * {
			flex: 1 1 100%;
		}
	}
</style>

