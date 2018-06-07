export const parseError = err =>
  new Promise((resolve, reject) =>
    isHttpError(err) ? resolve(parseHttpError(err)) : isException(err) ? resolve(err.message) : resolve('Unknown error'))

function parseHttpError (errorMessage) {
  const response = errorMessage.response
  if (response.status === 0 || response.status === -1) {
    errorMessage = 'Could not reach the application server!'
  } else if (response.status === 400 && response.data.message) {
    errorMessage = response.data.message
  } else if (response.status === 401) {
    errorMessage = 'You do not have permission for this operation!'
  } else if (response.status === 404) {
    errorMessage = 'Url ' + response.config.url + ' not found'
  } else if (response.data.exceptionMessage) {
    errorMessage = response.data.exceptionMessage
  } else if (response.data.message) {
    errorMessage = response.data.message
  } else {
    errorMessage = 'Unknown error'
  }
  return errorMessage
}

function isException (err) {
  return err instanceof Error
}

function isHttpError (err) {
  return err.response !== undefined
}
