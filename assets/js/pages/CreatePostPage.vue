<template>
	<div class="container">
		<b-card
			@submit="submit"
			title="Create Post"
			tag="section"
			class="ma-2">
			<b-form>
				<b-form-group
					label="Title:"
					label-for="title">
					<b-form-input
						v-model="form.title"
						id="title"
						type="text"
						required
						placeholder="Post title">
					</b-form-input>
				</b-form-group>
				<b-form-group
					label="Body"
					label-for="body">
					<b-form-textarea
						v-model="form.body"
						id="body"
						required
						:rows="6"
						placeholder="Post body">
					</b-form-textarea>
				</b-form-group>
				<b-button type="submit" variant="primary">Create</b-button>
			</b-form>
		</b-card>
	</div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

export default {
	data: () => ({
		...mapState(['loggedIn']),
		form: {
			title: '',
			body: ''
		}
	}),
	created() {
		if (!this.loggedIn) {
			this.$router.push({ name: 'login' })
		}
	},
	methods: {
		submit(e) {
			e.preventDefault();
			axios.post('api/posts/', this.form)
				.then(response => this.$router.push({ name: 'view-post', params: { id: response.data.id } }));
		}
	}
}
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
